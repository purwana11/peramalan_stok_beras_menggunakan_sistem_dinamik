document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.querySelector('.dropzone input[type="file"]');
    const fileName = document.querySelector(".file-name");

    if (fileInput && fileName) {
        fileInput.addEventListener("change", () => {
            if (fileInput.files.length) {
                fileName.textContent = fileInput.files[0].name;
                fileName.style.color = "#e2e8f0";
            } else {
                fileName.textContent = "Belum ada file dipilih";
                fileName.style.color = "";
            }
        });
    }
});
