// Toggle Dropdown in Sidebar

const sidebarDropBtnList = document.querySelectorAll(".drop-btn:not(.disabled)");
const classReg = /\/\d+\/class\/\d+\//;
const currentClassURL = window.location.href.match(classReg);

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

    // Highlight a link that matches the current Class URL
    if (currentClassURL && dropDownMenuChild.firstElementChild.href.match(classReg)[0] === currentClassURL[0]) {
      dropDownMenuChild.classList.add("class-active");
    }
  }
}


// Toggle Sidebar

const sidebarNav = document.querySelector("nav.sidebar-nav");
let isSidebarCollapsed = localStorage.getItem("isSidebarCollapsed");
let toggleSidebarButton = document.getElementById("toggle-nav-sidebar");
let hamburgerSVG = toggleSidebarButton.querySelector("#hamburger")
let closeSVG = toggleSidebarButton.querySelector("#close")

if (isSidebarCollapsed) {
  toggleSidebar();
  // Update timeout arguments If --dropdown-transition changes in index.css
  setTimeout(() => sidebarNav.style.display = null, 300);
} else {
  closeSVG.style.opacity = "1";
  sidebarNav.style.display = null;
}

function toggleSidebar() {
  if (sidebarNav.classList.contains("collapse")) {
    sidebarNav.classList.remove("collapse");
    localStorage.removeItem("isSidebarCollapsed");
    hamburgerSVG.style.opacity = null;
    closeSVG.style.opacity = "1";
  } else {
    sidebarNav.classList.add("collapse");
    localStorage.setItem("isSidebarCollapsed", "true");
    hamburgerSVG.style.opacity = "1";
    closeSVG.style.opacity = null;
  }
}

toggleSidebarButton.addEventListener("click", toggleSidebar);
