const fileInput = document.getElementById("id_image")
const previewImage = document.getElementById("selectedImage")

fileInput.addEventListener('change', event => {
    if(event.target.files.length > 0){
        previewImage.src = URL.createObjectURL(
            event.target.files[0]
        )
    }
})