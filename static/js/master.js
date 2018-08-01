//Copies the tables
function CopyStuff(el) {
   var body = document.body, range, sel;
   if (document.createRange && window.getSelection) {
       range = document.createRange();
       sel = window.getSelection();
       sel.removeAllRanges();
       try {
           range.selectNodeContents(el);
           sel.addRange(range);
       } catch (e) {
           range.selectNode(el);
           sel.addRange(range);
       }
   } else if (body.createTextRange) {
       range = body.createTextRange();
       range.moveToElementText(el);
       range.select();
   }
   document.execCommand("Copy");
   alert("Table copied to clipboard!")
   sel.removeAllRanges();
}

//When user scrolls from the top of page, scroll up button is displayed
function scrollFunction() {
  if (window.pageYOffset > 0) {
      $("#topBtn").attr("style", "display:block");
      $("#topbtn").attr("style", "display:block");
      $(".sidebar").css({
        "position":"fixed",
        "top":"0",
        "width":"23%",
      });
  } else {
      $("#topBtn").attr("style", "display:none");
      $("#topbtn").attr("style", "display:block");
      $(".sidebar").css({
        "position":"static",
        "width":"100%",
      });
  }
};

//Scrolls to top of page on click
function topFunction() {
  $("html, body").scrollTop(0);
};


//Add h4's to sidebar
function sidebarAppend(){
  var headings = document.getElementsByTagName("h4");
  var sidebar = document.getElementsByClassName("sidebar");

  for (var i = 0; i < headings.length; i++) {
      headings[i].id = headings[i].innerHTML.replace(/[^A-Z0-9]+/ig, "_");
      var link = document.createElement('a');
      link.className = "sidebar-button";
      link.href = '#' + headings[i].id;
      link.textContent = headings[i].innerHTML;

      sidebar[0].appendChild(link);
    };
  };


//Hides the sidebar on small screens since bootstrap doesn't seem to work

window.onload = function(){$("#topBtn").attr("style", "display:none");};
window.onload = function(){sidebarAppend()};
window.onscroll = function() {scrollFunction()};
