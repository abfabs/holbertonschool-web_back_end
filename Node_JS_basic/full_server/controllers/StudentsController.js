import { readDatabase } from '../utils.js';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const dbPath = process.argv[2];

    try {
      const fields = await readDatabase(dbPath);
      res.status(200).write('This is the list of our students\n');

      // Sort fields alphabetically (case-insensitive)
      Object.keys(fields)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
        .forEach((field) => {
          const names = fields[field];
          res.write(
            `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`
          );
        });

      res.end();
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const major = req.params.major;
    const dbPath = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const fields = await readDatabase(dbPath);
      if (!fields[major]) {
        res.status(200).send('List:');
        return;
      }
      const names = fields[major];
      res.status(200).send(`List: ${names.join(', ')}`);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }
}
