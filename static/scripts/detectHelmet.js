const selectImage = document.querySelector('.select-image');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.img-area');
const uploadForm = document.getElementById('uploadForm');

function isFileImage(file) {
    const acceptedImageTypes = ['image/jpeg', 'image/png', 'image/gif'];

    return acceptedImageTypes.includes(file.type);
}

let imageSelected = false

selectImage.addEventListener('click', function () {
    if (imageSelected) {
        uploadForm.submit();
    } else {
        inputFile.click();
    }
})
inputFile.addEventListener('change', function () {
    const image = this.files[0]
    console.log(image);
    if (isFileImage(image)) {
        if (image.size < 2000000) {
            const reader = new FileReader();
            reader.onload = () => {
                const allImg = imgArea.querySelectorAll('img');
                allImg.forEach(item => item.remove());
                const imgUrl = reader.result;
                const img = document.createElement('img');
                img.src = imgUrl;
                imgArea.appendChild(img);
                imgArea.classList.add('active');
                imgArea.dataset.img = image.name;
                selectImage.innerHTML = 'Run Detection';
                imageSelected = true
            }
            reader.readAsDataURL(image);
        }
        else {
            alert("Image size more than 2mb")
        }
    }
    else {
        alert("Select only Image File")
    }
});

