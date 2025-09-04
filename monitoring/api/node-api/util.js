const getRandomValue = (arr=[]) => {
    const randInd = Math.floor(Math.random()*arr.length)
    return arr[randInd]
}

export const doHeavyTask = async() =>{
    const shouldThrowErr = getRandomValue([1,2,3,4]) === 4
    if(shouldThrowErr){
        throw new Error(getRandomValue([
            "DB Failure",
            "Access Denied",
            "Too many requests",
            "Not found"
        ]))
    }
    const ms = getRandomValue([100, 150, 200, 300, 500])
    return new Promise(resolve=>setTimeout(()=>resolve(ms), ms))
}