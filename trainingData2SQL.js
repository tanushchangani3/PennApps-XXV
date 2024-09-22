const mysql = require('mysql2');
const fs = require('fs');

// MySQL connection
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root',
  database: 'PennApp'
});

// Read and parse JSON file
fs.readFile('trainingData.json', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the JSON file:', err);
    return;
  }

  // Parse the JSON data (though it's not necessary for this case, we want to validate the JSON)
  const alumniData = JSON.parse(data);

  // Prepare SQL query for inserting the entire JSON object into the `profile_data` column
  const query = 'INSERT INTO alumni_data (profile_data) VALUES (?)';

  // Insert each JSON object into the table
  alumniData.forEach(alumni => {
    connection.query(query, [JSON.stringify(alumni)], (error, results) => {
      if (error) {
        console.error('Error inserting data:', error);
      } else {
        console.log('Data inserted successfully:', results);
      }
    });
  });

  // Close the connection
  connection.end();
});
