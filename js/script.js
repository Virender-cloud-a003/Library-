// JS for form messages (optional)
document.addEventListener("DOMContentLoaded", function () {
  const bookForm = document.getElementById('bookForm');
  const memberForm = document.getElementById('memberForm');

  if (bookForm) {
    bookForm.addEventListener('submit', function (e) {
      e.preventDefault();
      document.getElementById('bookMessage').textContent = "✅ Book added successfully!";
      bookForm.reset();
    });
  }

  if (memberForm) {
    memberForm.addEventListener('submit', function (e) {
      e.preventDefault();
      document.getElementById('memberMessage').textContent = "✅ Member added successfully!";
      memberForm.reset();
    });
  }
});
