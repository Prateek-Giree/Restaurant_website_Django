document.addEventListener('DOMContentLoaded', function () {
    // Get all elements with the class "enlargeable"
    const images = document.querySelectorAll('.enlargeable')

    // Add a click event listener to each image
    images.forEach((image) => {
        image.addEventListener('click', function () {
            // Toggle the "enlarged" class for the clicked image
            this.classList.toggle('enlarged')
        })
    })
})