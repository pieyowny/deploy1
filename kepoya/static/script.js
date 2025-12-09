/* Since we switched to Python Flask, we removed the logic 
   that generates IDs here. Python handles the database now! 
*/

function copyText(id) {
  // Get the input field
  var copyText = document.getElementById(id);
  
  // Select the text field
  copyText.select();
  copyText.setSelectionRange(0, 99999); // For mobile devices

  // Copy the text inside the text field
  navigator.clipboard.writeText(copyText.value);
  
  alert("Link berhasil disalin: " + copyText.value);
}