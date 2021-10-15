const sidebarDropBtnList = document.querySelectorAll(".drop-btn:not(.disabled)");

for (const sidebarDropBtnElement of sidebarDropBtnList) {
    const dropDownMenu = sidebarDropBtnElement.parentElement.querySelector('.drop-down-menu')
    const btn = sidebarDropBtnElement.parentElement;
    const dropDownMenuChildren = dropDownMenu.children;

    function toggleDropDown() {
        sidebarDropBtnElement.classList.toggle("clicked");
        btn.classList.toggle("expand");
        if (dropDownMenu.style.maxHeight) {
            dropDownMenu.style.maxHeight = null;
        } else {
            let dropDownMenuHeight = 0.0;
            for (const dropDownMenuChild of dropDownMenuChildren) {
                dropDownMenuHeight += dropDownMenuChild.offsetHeight + 0.4;
            }
            dropDownMenu.style.maxHeight = dropDownMenuHeight + "px";
        }
    }

    sidebarDropBtnElement.addEventListener('click', toggleDropDown);

    for (const dropDownMenuChild of dropDownMenuChildren) {
        dropDownMenuChild.addEventListener('click', toggleDropDown);
    }
}
