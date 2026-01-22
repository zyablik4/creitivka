const draggable  = document.getElementById('draggable')
const dropzone = document.getElementById('dropzone')

draggable.addEventListener('dragstart', (event) => {
    event.dataTransfer.setData('text', 'Элемент');
});

dropzone.addEventListener('dragover', (event) => {
    event.preventDefault();
});

dropzone.addEventListener('drop', (event) =>{
    event.preventDefault();
    dropzone.style.backgroundColor = 'green'
    const data = event.dataTransfer.getData('text')
    alert(data)
});