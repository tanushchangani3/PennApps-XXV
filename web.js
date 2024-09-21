const express = require("express")
const {connectToDB, getDB} = require('./db')

// Initialize app and middleware
const app = express()

// Do connections
let db
connectToDB((err) => {
    if (!err) {
        app.listen(3000, () => {
            console.log('app listening on port 3000')
        })
        db = getDB()
    }
})

// Route to fetch documents from DefaultTrainingSet
app.get('/PennApps2024', async (req, res) => {
    try {
        // Ensure db is connected
        if (!db) {
            return res.status(500).json({error: "Database not connected"})
        }

        // Fetch documents from MongoDB collection and sort by _id
        const docs = await db.collection('DefaultTrainingSet').find().sort({_id: 1}).toArray()
        
        // Return fetched documents
        res.status(200).json({mssg: "welcome to the api", data: docs})
    } catch (error) {
        console.error(error)
        res.status(500).json({error: "bro TF????"})
    }
})
