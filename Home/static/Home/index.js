// Toggle Dropdown in Sidebar

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
        dropDownMenuHeight += dropDownMenuChild.offsetHeight;
      }
      dropDownMenu.style.maxHeight = dropDownMenuHeight + "px";
    }
  }

  sidebarDropBtnElement.addEventListener('click', toggleDropDown);

  for (const dropDownMenuChild of dropDownMenuChildren) {
    dropDownMenuChild.addEventListener('click', toggleDropDown);
  }
}


// Toggle Sidebar

const sidebarNav = document.querySelector("nav.sidebar-nav");
let isSidebarCollapsed = localStorage.getItem("isSidebarCollapsed");
let toggleSidebarButton = document.getElementById("toggle-nav-sidebar");

if (isSidebarCollapsed) {
  toggleSidebar();
  // Update timeout arguments If --dropdown-transition changes in index.css
  setTimeout(() => sidebarNav.style.display = null, 300);
} else {
  sidebarNav.style.display = null;
}

function toggleSidebar() {
  if (sidebarNav.classList.contains("collapse")) {
    sidebarNav.classList.remove("collapse");
    localStorage.removeItem("isSidebarCollapsed");
  } else {
    sidebarNav.classList.add("collapse");
    localStorage.setItem("isSidebarCollapsed", "true");
  }
}

toggleSidebarButton.addEventListener("click", toggleSidebar);
