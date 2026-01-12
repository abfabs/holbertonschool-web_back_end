const fs = require('fs');

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  // Split lines and remove empty lines
  const lines = data.split('\n').filter((line) => line.trim() !== '');
  if (lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }

  // Skip header
  const students = lines.slice(1).map((line) => line.split(','));

  console.log(`Number of students: ${students.length}`);

  const fields = {};

  students.forEach(([firstName, , field]) => {
    const cleanField = field.trim();
    const cleanName = firstName.trim();
    if (!fields[cleanField]) {
      fields[cleanField] = [];
    }
    fields[cleanField].push(cleanName);
  });

  for (const field in fields) {
    console.log(
      `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
    );
  }
}

module.exports = countStudents;
