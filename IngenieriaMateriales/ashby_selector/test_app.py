"""
Pruebas unitarias para AshbyChart Selector
Para ejecutar: python -m pytest test_app.py -v
"""

import pytest
import sys
import os

# Agregar el directorio actual al path para importar app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import MaterialProperties, MaterialFamily, MaterialDatabase, AshbyChartGenerator, MaterialFilter

class TestMaterialProperties:
    """Pruebas para la clase MaterialProperties"""
    
    def test_material_creation(self):
        """Prueba la creación de un material"""
        material = MaterialProperties(
            name="Test Material",
            density=(1000, 2000),
            young_modulus=(10, 20),
            yield_strength=(100, 200),
            fracture_toughness=(5, 10),
            thermal_conductivity=(0.1, 0.2),
            thermal_expansion=(10, 20),
            max_temp=(100, 200),
            price=(1, 5)
        )
        
        assert material.name == "Test Material"
        assert material.density == (1000, 2000)
        assert material.young_modulus == (10, 20)

class TestMaterialDatabase:
    """Pruebas para la clase MaterialDatabase"""
    
    def setup_method(self):
        """Configuración para cada prueba"""
        self.db = MaterialDatabase()
    
    def test_database_initialization(self):
        """Prueba que la base de datos se inicialice correctamente"""
        assert len(self.db.families) > 0
        assert "Aceros" in self.db.families
        assert "Aleaciones de Aluminio" in self.db.families
    
    def test_get_family_bounds(self):
        """Prueba el cálculo de límites de familia"""
        x_min, x_max, y_min, y_max = self.db.get_family_bounds("Aceros", "density", "young_modulus")
        
        assert x_min is not None
        assert x_max is not None
        assert y_min is not None
        assert y_max is not None
        assert x_min <= x_max
        assert y_min <= y_max
    
    def test_add_material(self):
        """Prueba agregar un material a una familia existente"""
        initial_count = len(self.db.families["Aceros"].materials)
        
        new_material = MaterialProperties(
            name="Acero de Prueba",
            density=(7500, 7600),
            young_modulus=(200, 205),
            yield_strength=(300, 350),
            fracture_toughness=(60, 80),
            thermal_conductivity=(45, 48),
            thermal_expansion=(11, 12),
            max_temp=(550, 580),
            price=(1.0, 1.5)
        )
        
        self.db.add_material("Aceros", new_material)
        
        assert len(self.db.families["Aceros"].materials) == initial_count + 1
        assert self.db.families["Aceros"].materials[-1].name == "Acero de Prueba"
    
    def test_add_family(self):
        """Prueba agregar una nueva familia"""
        initial_count = len(self.db.families)
        
        new_family = MaterialFamily(
            name="Materiales de Prueba",
            color="#FF0000",
            materials=[]
        )
        
        self.db.add_family(new_family)
        
        assert len(self.db.families) == initial_count + 1
        assert "Materiales de Prueba" in self.db.families

class TestAshbyChartGenerator:
    """Pruebas para la clase AshbyChartGenerator"""
    
    def setup_method(self):
        """Configuración para cada prueba"""
        self.db = MaterialDatabase()
        self.chart_gen = AshbyChartGenerator(self.db)
    
    def test_generate_ellipse_points(self):
        """Prueba la generación de puntos de elipse"""
        x_points, y_points = self.chart_gen.generate_ellipse_points(100, 200, 50, 100)
        
        assert len(x_points) > 0
        assert len(y_points) > 0
        assert len(x_points) == len(y_points)
        assert min(x_points) >= 100
        assert max(x_points) <= 200
    
    def test_generate_ellipse_points_invalid(self):
        """Prueba la generación de elipse con valores inválidos"""
        x_points, y_points = self.chart_gen.generate_ellipse_points(-100, 200, 50, 100)
        
        assert len(x_points) == 0
        assert len(y_points) == 0
    
    def test_create_ashby_chart(self):
        """Prueba la creación de gráficos de Ashby"""
        fig = self.chart_gen.create_ashby_chart("density", "young_modulus")
        
        assert fig is not None
        assert len(fig.data) > 0
        assert fig.layout.xaxis.title.text == "Densidad (kg/m³)"
        assert fig.layout.yaxis.title.text == "Módulo de Young (GPa)"

class TestMaterialFilter:
    """Pruebas para la clase MaterialFilter"""
    
    def setup_method(self):
        """Configuración para cada prueba"""
        self.db = MaterialDatabase()
        self.filter = MaterialFilter(self.db)
    
    def test_apply_no_filters(self):
        """Prueba aplicar filtros vacíos"""
        result = self.filter.apply_numeric_filters([])
        
        assert len(result) == len(self.db.families)
    
    def test_apply_density_filter(self):
        """Prueba filtro por densidad"""
        filters = [{'property': 'density', 'operator': '<', 'value': 3000}]
        result = self.filter.apply_numeric_filters(filters)
        
        # Debe incluir polímeros y excluir metales pesados
        assert "Termoplásticos" in result
        assert len(result) < len(self.db.families)
    
    def test_apply_multiple_filters(self):
        """Prueba múltiples filtros"""
        filters = [
            {'property': 'density', 'operator': '<', 'value': 5000},
            {'property': 'young_modulus', 'operator': '>', 'value': 50}
        ]
        result = self.filter.apply_numeric_filters(filters)
        
        # Debe filtrar efectivamente
        assert len(result) <= len(self.db.families)
        
        # Verificar que los materiales restantes cumplan las condiciones
        for family_name in result:
            family = self.db.families[family_name]
            
            # Al menos un material debe cumplir ambas condiciones
            passes_density = any(mat.density[0] < 5000 for mat in family.materials)
            passes_young = any(mat.young_modulus[1] > 50 for mat in family.materials)
            
            assert passes_density and passes_young

class TestIntegration:
    """Pruebas de integración"""
    
    def setup_method(self):
        """Configuración para cada prueba"""
        self.db = MaterialDatabase()
        self.chart_gen = AshbyChartGenerator(self.db)
        self.filter = MaterialFilter(self.db)
    
    def test_full_workflow(self):
        """Prueba el flujo completo de trabajo"""
        # 1. Aplicar filtros
        filters = [{'property': 'density', 'operator': '<', 'value': 3000}]
        filtered_families = self.filter.apply_numeric_filters(filters)
        
        # 2. Generar gráfico con familias filtradas
        fig = self.chart_gen.create_ashby_chart("density", "young_modulus", filtered_families)
        
        # 3. Verificar que el gráfico se generó correctamente
        assert fig is not None
        assert len(fig.data) <= len(self.db.families)
        
        # 4. Verificar que solo aparecen familias filtradas
        trace_names = [trace.name for trace in fig.data]
        for name in trace_names:
            assert name in filtered_families

# Configuración para pytest
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
