import app from './app'
import { SERVER_PORT } from './config/environment'

app.listen(SERVER_PORT, () => {
  console.log('Server is running on port - ', SERVER_PORT)
})
