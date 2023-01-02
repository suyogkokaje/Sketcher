const SelecttionArea = document.querySelector("#Select-area"),
    fileInput = document.querySelector(".file-input");
let preview = document.getElementById("file-preview");
let removeImage = document.getElementById("remove-img");

// Remove Button Bydefault Hidden
removeImage.style.display = "none";

// Remove Button Wait For Click to Action 
removeImage.addEventListener("click", () => {
    preview.src = "";
    preview.style.display = "none";
    SelecttionArea.style.display = "";
    removeImage.style.display = "none";
    fileInput.value = "";
});

// Select-Are  wait for click to acation file-input
SelecttionArea.addEventListener("click", () => {
    fileInput.click();
});


fileInput.onchange = ({ target }) => {
    let file = target.files[0];
    let src = URL.createObjectURL(file)
    preview.src = src;
    SelecttionArea.style.display = "none";
    removeImage.style.display = "";
    preview.style.display = '';
}