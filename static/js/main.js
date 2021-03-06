// IIFE
(function(){
    document.querySelector('#categoryInput').addEventListener('keydown', function(e){
        if(e.keyCode !== 13){
            return;
        }

        e.preventDefault();

        var categoryName = this.value;
        this.value = '';
        addNewCategory(categoryName);
        updateCategoryString();
    })

    // add category
    const addNewCategory = (name) => {
        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend', 
        `<li class="category">
            <span class="name">${name}</span>
            <span onclick="removeCategory(this)" class="btnRemove bold close-icon red-text"> x </span>
        </li>`
        )
    }
})()


// update category
const fetchCategoryArray = () => {
    var categories = []

    document.querySelectorAll('.category').forEach( (el) => {
        let name = el.querySelector('.name').innerHTML;
        if (name == '') return;

        categories.push(name);
    })

    return categories;
}


// join updated strings
const updateCategoryString = () => {
    let categories = fetchCategoryArray();
    document.querySelector('input[name="categoryString"]').value = categories.join(',');
}


// remove category
const removeCategory = (e) => {
    e.parentElement.remove();
    updateCategoryString()
}