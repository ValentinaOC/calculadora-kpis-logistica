import streamlit as st

st.set_page_config(page_title="Calculadora Logística", page_icon="📦", layout="centered")

st.title("Calculadora sencilla de Indicadores Logísticos")
st.markdown("Ingresa los datos de tu operación para calcular los principales KPIs.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    total_pedidos = st.number_input("Total de pedidos del período", min_value=1, value=100)
    pedidos_perfectos = st.number_input("Pedidos entregados perfectos", min_value=0, value=85)
    pedidos_tiempo = st.number_input("Pedidos entregados a tiempo", min_value=0, value=90)

with col2:
    unidades_despachadas = st.number_input("Unidades despachadas", min_value=1, value=500)
    unidades_devueltas = st.number_input("Unidades devueltas", min_value=0, value=20)
    costo_total = st.number_input("Costo total de operación ($)", min_value=0.0, value=10000000.0, step=100000.0)

st.divider()

# --- Cálculos ---
if st.button("Calcular indicadores", use_container_width=True):
    st.progress(0.85)

    otif = (pedidos_perfectos / total_pedidos) * 100
    tasa_devolucion = (unidades_devueltas / unidades_despachadas) * 100
    tasa_entrega_tiempo = (pedidos_tiempo / total_pedidos) * 100
    costo_por_pedido = costo_total / total_pedidos

    st.subheader("Resultados")

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            label="✅ OTIF (Pedidos perfectos)",
            value=f"{otif:.1f}%",
            delta="Meta: ≥ 95%" if otif >= 95 else f"{otif - 95:.1f}% vs meta",
        )
        st.metric(
            label="🔄 Tasa de devolución",
            value=f"{tasa_devolucion:.1f}%",
            delta="✓ Bajo control" if tasa_devolucion <= 5 else "⚠ Revisar",
        )

    with col4:
        st.metric(
            label="⏱ Entregas a tiempo",
            value=f"{tasa_entrega_tiempo:.1f}%",
            delta="Meta: ≥ 95%" if tasa_entrega_tiempo >= 95 else f"{tasa_entrega_tiempo - 95:.1f}% vs meta",
        )
        st.metric(
            label="💰 Costo por pedido",
            value=f"${costo_por_pedido:,.0f}",
        )

    st.divider()

    # Semáforo de salud general
    puntaje = 0
    if otif >= 95: puntaje += 1
    if tasa_devolucion <= 5: puntaje += 1
    if tasa_entrega_tiempo >= 95: puntaje += 1

    if puntaje == 3:
        st.success("🟢 Operación en buen estado — todos los indicadores en meta.")
    elif puntaje == 2:
        st.warning("🟡 Operación aceptable — hay indicadores por mejorar.")
    else:
        st.error("🔴 Operación con alertas — revisar procesos críticos.")
    
