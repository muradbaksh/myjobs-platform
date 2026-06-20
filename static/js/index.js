//--------------------For Messages-------------------
document.addEventListener('DOMContentLoaded', function () {

    setTimeout(function () {

        document.querySelectorAll('.auto-alert').forEach(function(alert){

            let bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();

        });

    }, 4000); 

});



// ----------------Search scroll--------------------
document.addEventListener("DOMContentLoaded", function () {

    const params = new URLSearchParams(window.location.search);

    if (params.get("q")) {

        const companiesSection = document.getElementById("companies");

        if (companiesSection) {

            companiesSection.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }
    }

});

/*------------------ Bottom To Top Button ----------------------------*/
const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    backToTop.classList.add("show");
  } else {
    backToTop.classList.remove("show");
  }
});

backToTop.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});


// -----------------------Review alert---------------------------
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form-card form');
    const ratingInputs = form.querySelectorAll('input[type="number"][min="1"][max="5"]');

    ratingInputs.forEach(function (input) {
        input.addEventListener('input', function () {
            const val = Number(input.value);
            if (input.value !== '' && (val < 1 || val > 5)) {
                input.setCustomValidity('Please enter a number between 1 and 5.');
                input.reportValidity();
            } else {
                input.setCustomValidity('');
            }
        });
    });
});