const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('preview');
const previewSection = document.getElementById('previewSection')
const submitButton = document.getElementById('submitButton');

submitButton.style.display = 'none'
previewSection.style.display = 'none'

imageInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            previewSection.style.display = 'inline-block'
            preview.src = e.target.result;
            submitButton.style.display = 'inline-block';
        };

        reader.readAsDataURL(file);
    } else {
        preview.src = '';
        submitButton.style.display = 'none';
        previewSection.style.display = 'none'
    }
});