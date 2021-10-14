const sidebarDropBtnList = document.querySelectorAll(".drop-btn:not(.disabled)");

for (const sidebarDropBtnElement of sidebarDropBtnList) {
    const dropDownMenu = sidebarDropBtnElement.parentElement.querySelector('.drop-down-menu')
    const btn = sidebarDropBtnElement.parentElement;
    const dropDownMenuChildren = dropDownMenu.children;

    let dropDownMenuHeight = 0;
    for (const dropDownMenuChild of dropDownMenuChildren) {
        dropDownMenuHeight += dropDownMenuChild.clientHeight;
    }

    sidebarDropBtnElement.onclick = () => {
        sidebarDropBtnElement.classList.toggle("clicked");
        btn.classList.toggle("expand");
        if (dropDownMenu.style.maxHeight) {
            dropDownMenu.style.maxHeight = null;
        } else {
            dropDownMenu.style.maxHeight = (dropDownMenuHeight / 10) + "rem";
        }
    }
}
