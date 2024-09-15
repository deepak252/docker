const express = require('express')
const db = require('../db');
const app = express()
app.use(express.json())

const PORT = process.env.PORT || 8000

app.get('/', async (req, res)=>{
    try{
        const data = await db.query('SELECT * FROM schools')
        res.status(200).json({
            message: "Successfully fetched data",
            data
        })
    }catch(e){
        console.log(e);
        res.sendStatus(500)
    }
})

app.post('/', async (req, res)=>{
    const {name, location} = req.body;
    try{
        await db.query('INSERT INTO schools (name, address) VALUES ($1, $e)', [name, location])
        res.status(200).json({
            message: "Successfully added child"
        })
    }catch(e){
        console.log(e);
        res.sendStatus(500)
    }
})

app.get('/setup', async (req, res)=>{
    try{
        await db.query('CREATE TABLE schools(id SERIAL PRIMARY KEY, name VARCHAR(100), address VARCHAR(100))')
        res.status(200).json({
            message: "Successfully created table"
        })
    }catch(e){
        console.log(e);
        res.sendStatus(500)
    }
})
app.listen(PORT, ()=>{
    console.log('Server is running port', PORT);
})