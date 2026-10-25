const form =
    document.getElementById("predictionForm");

const predictBtn =
    document.getElementById("predictBtn");

const resetBtn =
    document.getElementById("resetBtn");

const emptyResult =
    document.getElementById("emptyResult");

const loading =
    document.getElementById("loading");

const predictionResult =
    document.getElementById("predictionResult");

const prediction =
    document.getElementById("prediction");

const recommended =
    document.getElementById("recommended");

const newPrediction =
    document.getElementById("newPrediction");

const area =
    document.getElementById("op_area");

const areaValue =
    document.getElementById("areaValue");


/* ================= AREA SLIDER ================= */

area.addEventListener("input", function () {

    areaValue.textContent =
        parseFloat(this.value).toFixed(1);

});


/* ================= FORM SUBMIT ================= */

form.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        /* Show loading */

        emptyResult.style.display = "none";

        predictionResult.style.display = "none";

        loading.style.display = "flex";

        predictBtn.disabled = true;

        predictBtn.innerHTML =
            "⏳ Analyzing...";


        /* Collect data */

        const data = {

            week:
                document.getElementById(
                    "week"
                ).value,

            center_id:
                document.getElementById(
                    "center_id"
                ).value,

            meal_id:
                document.getElementById(
                    "meal_id"
                ).value,

            checkout_price:
                document.getElementById(
                    "checkout_price"
                ).value,

            base_price:
                document.getElementById(
                    "base_price"
                ).value,

            promotion:
                document.getElementById(
                    "promotion"
                ).checked ? 1 : 0,

            featured:
                document.getElementById(
                    "featured"
                ).checked ? 1 : 0,

            category:
                document.getElementById(
                    "category"
                ).value,

            cuisine:
                document.getElementById(
                    "cuisine"
                ).value,

            center_type:
                document.getElementById(
                    "center_type"
                ).value,

            op_area:
                document.getElementById(
                    "op_area"
                ).value
        };


        try {

            /* Send to Flask */

            const response =
                await fetch(
                    "/predict",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(data)
                    }
                );


            const result =
                await response.json();


            if (!result.success) {

                throw new Error(
                    result.error
                );

            }


            /* Display prediction */

            prediction.textContent =
                result.prediction;

            recommended.textContent =
                result.recommended;


            loading.style.display =
                "none";

            predictionResult.style.display =
                "flex";


        } catch (error) {

            loading.style.display =
                "none";

            emptyResult.style.display =
                "flex";

            alert(
                "Prediction failed: " +
                error.message
            );

        }


        predictBtn.disabled = false;

        predictBtn.innerHTML =
            "🔮 Predict Food Demand";

    }
);


/* ================= RESET ================= */

resetBtn.addEventListener(
    "click",
    function () {

        form.reset();

        area.value = 4;

        areaValue.textContent = "4.0";

        predictionResult.style.display =
            "none";

        loading.style.display =
            "none";

        emptyResult.style.display =
            "flex";

    }
);


/* ================= NEW PREDICTION ================= */

newPrediction.addEventListener(
    "click",
    function () {

        predictionResult.style.display =
            "none";

        emptyResult.style.display =
            "flex";

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    }
);