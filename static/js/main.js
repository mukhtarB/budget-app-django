// IIFY
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

    const addNewCategory = (name) => {
        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend', 
        `<li class="category">
            <span class="name">${name}</span>
            <span onclick="removeCategory(this)" class="btnRemove bold">x</span>
        </li>`
        )
    }
})()