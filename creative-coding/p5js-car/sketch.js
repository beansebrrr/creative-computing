const canvasWidth = 400
const canvasHeight = 400

function setup() {
  createCanvas(canvasWidth, canvasHeight);
}

function draw() {
  background(71, 97, 82);

  /* Car base */
  baseLength = canvasWidth-100
  baseHeight = 45
  baseXpos = canvasWidth/2-baseLength/2
  baseYpos = canvasHeight/2+baseHeight/2

  beginShape()

  vertex(baseXpos, baseYpos+baseHeight); // topleft
  vertex(baseXpos+baseLength, baseYpos+baseHeight);
  vertex(baseXpos+baseLength, baseYpos);
  vertex(baseXpos, baseYpos);
  
  endShape();
  
  /* Hood */
  hoodLength = baseLength / 3.9

  beginShape()
  vertex(baseXpos, baseYpos); // very left
  vertex(baseXpos+hoodLength, baseYpos-10);
  vertex(baseXpos+hoodLength, baseYpos);
  endShape()

  /* Cockpit */
  cockpitLength = baseLength / 1.6
  cockpitHeight = baseHeight
  
  beginShape()
  vertex(baseXpos+(hoodLength*0.9), baseYpos); // bottom left
  vertex(baseXpos+hoodLength, baseYpos-cockpitHeight);
  vertex(baseXpos+(hoodLength*0.9)+cockpitLength, baseYpos-cockpitHeight);
  vertex(baseXpos+hoodLength+cockpitLength, baseYpos);
  endShape()
  
  /* Wheels */
  tyreSize = 50
  circle (
    baseXpos+(baseLength/5), baseYpos+baseHeight,
    tyreSize
  )
  circle (
    baseXpos+baseLength-(baseLength/5), baseYpos+(baseHeight),
    tyreSize
  )

  wheelSize = tyreSize / 2
  circle (
    baseXpos+(baseLength/5), baseYpos+baseHeight,
    wheelSize
  )
  circle (
    baseXpos+baseLength-(baseLength/5), baseYpos+(baseHeight),
    wheelSize
  )
}
