                    young_min = st.number_input("Módulo Young mín (GPa):", min_value=0.0, value=10.0)
                    yield_min = st.number_input("Límite Elástico mín (MPa):", min_value=0.0, value=50.0)
                    fracture_min = st.number_input("Tenacidad mín (MPa√m):", min_value=0.0, value=1.0)
                    thermal_cond_min = st.number_input("Cond. Térmica mín (W/m·K):", min_value=0.0, value=0.1)
                    thermal_exp_min = st.number_input("Exp. Térmica mín (µm/m°C):", min_value=-10.0, value=5.0)
                    temp_min = st.number_input("Temp. Máx. mín (°C):", min_value=0.0, value=100.0)
                    price_min = st.number_input("Precio mín (€/kg):", min_value=0.0, value=1.0)
                
                with col2:
                    density_max = st.number_input("Densidad máx (kg/m³):", min_value=0.0, value=2000.0)
                    young_max = st.number_input("Módulo Young máx (GPa):", min_value=0.0, value=20.0)
                    yield_max = st.number_input("Límite Elástico máx (MPa):", min_value=0.0, value=100.0)
                    fracture_max = st.number_input("Tenacidad máx (MPa√m):", min_value=0.0, value=5.0)
                    thermal_cond_max = st.number_input("Cond. Térmica máx (W/m·K):", min_value=0.0, value=1.0)
                    thermal_exp_max = st.number_input("Exp. Térmica máx (µm/m°C):", min_value=-5.0, value=15.0)
                    temp_max = st.number_input("Temp. Máx. máx (°C):", min_value=0.0, value=200.0)
                    price_max = st.number_input("Precio máx (€/kg):", min_value=0.0, value=5.0)
                
                if st.form_submit_button("➕ Agregar Material"):
                    if material_name:
                        new_material = MaterialProperties(
                            name=material_name,
                            density=(density_min, density_max),
                            young_modulus=(young_min, young_max),
                            yield_strength=(yield_min, yield_max),
                            fracture_toughness=(fracture_min, fracture_max),
                            thermal_conductivity=(thermal_cond_min, thermal_cond_max),
                            thermal_expansion=(thermal_exp_min, thermal_exp_max),
                            max_temp=(temp_min, temp_max),
                            price=(price_min, price_max)
                        )
                        
                        st.session_state.database.add_material(selected_family, new_material)
                        st.success(f"Material '{material_name}' agregado a la familia '{selected_family}'")
                        st.rerun()
                    else:
                        st.error("Por favor ingrese un nombre para el material")
        
        with tab2:
            st.markdown("**Crear nueva familia de materiales**")
            
            with st.form("add_family_form"):
                family_name = st.text_input("Nombre de la familia:")
                family_color = st.color_picker("Color para la familia:", value="#FF5733")
                
                if st.form_submit_button("📁 Crear Familia"):
                    if family_name and family_name not in st.session_state.database.families:
                        new_family = MaterialFamily(
                            name=family_name,
                            color=family_color,
                            materials=[]
                        )
                        st.session_state.database.add_family(new_family)
                        st.success(f"Familia '{family_name}' creada exitosamente")
                        st.rerun()
                    elif family_name in st.session_state.database.families:
                        st.error("Ya existe una familia con ese nombre")
                    else:
                        st.error("Por favor ingrese un nombre para la familia")
        
        with tab3:
            st.markdown("**Exportar base de datos a archivo JSON**")
            
            if st.button("💾 Exportar a JSON"):
                filename = "materials_database.json"
                st.session_state.database.export_to_json(filename)
                
                # Leer el archivo para descarga
                with open(filename, 'r', encoding='utf-8') as f:
                    json_data = f.read()
                
                st.download_button(
                    label="📥 Descargar archivo JSON",
                    data=json_data,
                    file_name=filename,
                    mime="application/json"
                )
                
                st.success("Base de datos exportada exitosamente")
    
    # Información adicional
    st.markdown("---")
    with st.expander("ℹ️ Información sobre el Método Ashby"):
        st.markdown("""
        ## 📚 Método de Selección de Materiales de Ashby
        
        El método desarrollado por Michael Ashby es una herramienta sistemática para la selección de materiales 
        basada en el análisis de propiedades mediante gráficos logarítmicos.
        
        ### 🎯 Características principales:
        
        - **Gráficos de Propiedades**: Visualización logarítmica que permite comparar materiales con rangos 
          de propiedades muy diferentes
        - **Elipses de Familias**: Cada familia de materiales se representa como una elipse que abarca 
          el rango de propiedades de todos los materiales en esa familia
        - **Índices de Rendimiento**: Líneas que representan combinaciones de propiedades importantes 
          para aplicaciones específicas (ej: E/ρ para rigidez con mínimo peso)
        - **Filtros de Selección**: Herramientas para aplicar restricciones y reducir el espacio de soluciones
        
        ### 📊 Índices de Rendimiento Comunes:
        
        - **E/ρ**: Rigidez específica (pendiente = 1)
        - **E^(1/2)/ρ**: Frecuencia de vibración (pendiente = 0.5)
        - **σ/ρ**: Resistencia específica (pendiente = 1)
        - **E^(1/3)/ρ**: Deflexión mínima en vigas (pendiente = 0.33)
        
        ### 🔄 Proceso de Selección:
        
        1. **Traducción**: Convertir requisitos de diseño en propiedades de materiales
        2. **Screening**: Aplicar filtros para eliminar materiales inadecuados
        3. **Ranking**: Usar índices de rendimiento para clasificar candidatos
        4. **Documentación**: Investigar en detalle los materiales finalistas
        """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; font-size: 14px;'>
            🔬 AshbyChart Selector - Desarrollado con Python y Streamlit<br>
            Implementación del Método de Selección de Materiales de Michael Ashby
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
