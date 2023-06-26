const selectImage = document.querySelector('.select-image');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.img-area');
const uploadForm = document.getElementById('uploadForm');

function isFileImage(file) {
    const acceptedImageTypes = ['image/jpeg', 'image/png', 'image/gif'];

    return acceptedImageTypes.includes(file.type);
}

selectImage.addEventListener('click',function(){
    inputFile.click();
})


inputFile.addEventListener('change', function () {
    const image = this.files[0]
    console.log(image);
    if (image.size < 2000000) {
        if(isFileImage(image)){
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
            }
            if (inputFile.files.length > 0) {

                uploadForm.submit();
            }
            reader.readAsDataURL(image);
        }
        else{
            alert("Select only Image File")
        } 
    }
    else {
        alert("Image size more than 2mb")
    }
});

