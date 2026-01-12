import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      if (lines.length <= 1) {
        resolve({});
        return;
      }

      const students = lines.slice(1).map((line) => line.split(','));
      const fields = {};

      students.forEach(([firstName, , field]) => {
        const f = field.trim();
        const name = firstName.trim();
        if (!fields[f]) fields[f] = [];
        fields[f].push(name);
      });

      resolve(fields);
    });
  });
}
