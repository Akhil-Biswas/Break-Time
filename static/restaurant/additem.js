const inputFile = document.querySelector("#uploadfile");
const Preview = document.querySelector("#imagePreview");
const Name = document.querySelector("#imageName");
const imageSize = document.querySelector("#imageSize");
const errorDisplay = document.querySelector("#errorDisplay");

inputFile.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        if (!['image/jpeg', 'image/jpg'].includes(file.type)) {
            errorDisplay.textContent = "Only JPG/JPEG allowed";
            Preview.src = "";
            imageSize.style.display = "none";
            return;
        }
        errorDisplay.textContent = "";
        Name.textContent = file.name;
        imageSize.textContent = Math.round(file.size / 1024) + " kb";
        imageSize.style.display = "block";

        const reader = new FileReader();
        reader.onload = () => Preview.src = reader.result;
        reader.readAsDataURL(file);
    } else {
        Preview.src = "../static/images/items/default.jpg";
        imageSize.style.display = "none";
    }
});