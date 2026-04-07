import streamlit as st

st.set_page_config(page_title="Kairo AI Energy Advisor", layout="centered")

# Header
st.title("⚡ Kairo AI – Renewable Energy Advisor")
st.markdown("Helping you make smarter energy decisions using AI-driven insights.")
st.markdown("---")

# User Inputs
st.header("🔍 Tell us about your energy needs")

location = st.text_input("📍 Your Location (e.g., Ghana, Kenya, Canada)")
energy_use = st.slider("⚡ Daily Energy Usage (kWh)", 1, 50, 5)
budget = st.selectbox("💰 Your Budget Level", ["Low", "Medium", "High"])
usage_type = st.selectbox("🏠 Usage Type", ["Home", "Small Business", "Farm"])

st.markdown("---")

# Logic
if st.button("🔋 Get Recommendation"):

    # Determine system size
    if energy_use <= 5:
        system = "Small Solar Kit"
        panels = "1-3 solar panels"
        battery = "Small battery storage"
        cost = "$300 – $800"
    elif energy_use <= 15:
        system = "Medium Solar System"
        panels = "4-8 solar panels"
        battery = "Medium battery storage"
        cost = "$800 – $2,000"
    else:
        system = "Full Solar Setup"
        panels = "10+ solar panels"
        battery = "Large battery storage"
        cost = "$2,000+"

    # Adjust based on budget
    if budget == "Low":
        budget_advice = "Start with a smaller system and scale over time."
    elif budget == "Medium":
        budget_advice = "You can afford a balanced system with battery backup."
    else:
        budget_advice = "You can invest in a high-efficiency system with long-term savings."

    # Location insight
    if location:
        location_advice = f"{location} has strong solar potential, making solar a reliable option."
    else:
        location_advice = "Your location likely supports solar energy adoption."

    # Usage insight
    if usage_type == "Farm":
        usage_advice = "Consider solar-powered irrigation or storage systems."
    elif usage_type == "Small Business":
        usage_advice = "Ensure stable power supply for operations and reduce outages."
    else:
        usage_advice = "Focus on reducing household energy costs and improving reliability."

    # Output
    st.header("🔋 Your Energy Plan")

    st.subheader("⚡ Recommended System")
    st.write(f"**System Type:** {system}")
    st.write(f"**Solar Panels:** {panels}")
    st.write(f"**Battery:** {battery}")
    st.write(f"**Estimated Cost:** {cost}")

    st.markdown("---")

    st.subheader("🧠 Kairo AI Insights")
    st.write(f"• {location_advice}")
    st.write(f"• {budget_advice}")
    st.write(f"• {usage_advice}")

    st.markdown("---")

    st.subheader("🌱 Impact")
    st.write(
        "Switching to solar energy can reduce electricity costs, improve energy access, "
        "and support sustainable development in your community."
    )

    st.success("✅ Recommendation generated successfully!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ as part of AmunRa – AI x Renewable Energy x Community Impact")