const canvasWidth = 400
const canvasHeight = 400

function setup() {
  createCanvas(canvasWidth, canvasHeight);
}


function draw() {
  background(98, 153, 87);

  // body
  squareSize = 150
  const squarePosX = canvasWidth/2 - squareSize/2
  const squarePosY = canvasHeight/2 - squareSize/2
  fill(245, 164, 88)
  rect(squarePosX, squarePosY, squareSize)

  // roof
  roofHeight = squareSize * 0.60

  fill(140, 13, 17)
  triangle(
    squarePosX,             squarePosY, // left corner
    canvasWidth-squarePosX, squarePosY, // right corner
    canvasHeight/2,         squarePosY-roofHeight, // rooftop
  ) 

  // door
  doorWidth = 50
  fill(87, 75, 68)
  rect(400/2-doorWidth/2, 400/2, doorWidth, squareSize/2)

  // doorknob
  fill("gold")
  circle(canvasWidth/2-doorWidth/2+10, canvasHeight/2+squareSize/4, 10)
}
