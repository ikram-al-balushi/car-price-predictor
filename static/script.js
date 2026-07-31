// Slider live value updates
const sliders = [
    { id: "year", display: "year_val", format: (v) => v },
    { id: "mileage_km", display: "mileage_km_val", format: (v) => Number(v).toLocaleString() },
    { id: "engine_cc", display: "engine_cc_val", format: (v) => Number(v).toLocaleString() }
];

sliders.forEach(({ id, display, format }) => {
    const slider = document.getElementById(id);
    const label = document.getElementById(display);
    slider.addEventListener("input", () => {
        label.textContent = format(slider.value);
    });
});

// Predict button click
document.getElementById("predict-btn").addEventListener("click", async () => {
    const payload = {
        make: document.getElementById("make").value,
        model: document.getElementById("model").value,
        fuel_type: document.getElementById("fuel_type").value,
        transmission: document.getElementById("transmission").value,
        body_type: document.getElementById("body_type").value,
        city: document.getElementById("city").value,
        year: document.getElementById("year").value,
        mileage_km: document.getElementById("mileage_km").value,
        engine_cc: document.getElementById("engine_cc").value
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        document.getElementById("result-price").textContent = result.price;
        document.getElementById("result-card").classList.remove("hidden");
    } catch (error) {
        alert("Prediction failed. Make sure the server is running.");
    }
});
