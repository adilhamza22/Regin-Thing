const form = document.getElementById('crawl-form');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent default form submission behavior

  const platform = document.getElementById('platform').value;

  // Fetch data from backend based on selected platform (replace with actual API call)
  const response = await fetch(`/crawl?platform=${platform}`);
  console.log(response);
  const courses = await response.json();
  console.log(courses);

  // Create the table structure and populate it with course data
  const table = document.createElement('table');
  table.classList.add('courses-table'); // Add a CSS class for styling (optional)

  const tableHead = document.createElement('thead');
  const tableBody = document.createElement('tbody');

  // Define table header row
  const headerRow = document.createElement('tr');
  const titleCell = document.createElement('th');
  const instructorCell = document.createElement('th');
  const linkCell = document.createElement('th');

  titleCell.textContent = 'Title';
  instructorCell.textContent = 'Instructor';
  linkCell.textContent = 'Link';

  headerRow.appendChild(titleCell);
  headerRow.appendChild(instructorCell);
  headerRow.appendChild(linkCell);
  tableHead.appendChild(headerRow);

  // Populate table rows with course data
  courses.forEach(course => {
    
    const row = document.createElement('tr');
    const titleCell = document.createElement('td');
    const instructorCell = document.createElement('td');
    const linkCell = document.createElement('td');

    titleCell.textContent = course.title;
    instructorCell.textContent = course.instructor;
    linkCell.innerHTML = `<a href="${course.link}">${course.link}</a>`;  // Create a link with course URL

    row.appendChild(titleCell);
    row.appendChild(instructorCell);
    row.appendChild(linkCell);
    tableBody.appendChild(row);
  });

  table.appendChild(tableHead);
  table.appendChild(tableBody);
  resultsDiv.innerHTML = '';  // Clear previous results
  resultsDiv.appendChild(table);
  console.log(table);
});
