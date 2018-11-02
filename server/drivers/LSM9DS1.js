//https://pinout.xyz/pinout/sense_hat#
//https://www.npmjs.com/package/i2c-bus
const i2c = require('i2c-bus')

const LSM9DS1_A_ADDRESS_R    = 0x1c
const LSM9DS1_CTR1           = 0x20
const LSM9DS1_CTR3           = 0x22
const LSM9DS1_STATUS_REG_M   = 0x27
const LSM9DS1_OUT_X_L_M      = 0x28
const LSM9DS1_OUT_X_H_M      = 0x29
const LSM9DS1_OUT_Y_L_M      = 0x2A
const LSM9DS1_OUT_Y_H_M      = 0x2B
const LSM9DS1_OUT_Z_L_M      = 0x2C
const LSM9DS1_OUT_Z_H_M      = 0x2D

initialized = false
X = 0
Y = 0
Z = 0
abs = 0

function init(){
  initialized = true
  i2c1 = i2c.openSync(1)

  //Calibration
  //Temperature compensation off, Ultra-high-performance mode, ODR 80 Hz
  i2c1.writeByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_CTR1,0x7C)
  //Continuous-conversion mode
  i2c1.writeByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_CTR3,0x00)
  i2c1.closeSync()
}

function turnOff(){
  initialized = false
  i2c1 = i2c.openSync(1)

  //Power-down mode
  i2c1.writeByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_CTR3,0x03)

  i2c1.closeSync()
}

function readMagnetometer(){
  if(!initialized){init()}

  i2c1 = i2c.openSync(1)
  //1111 1111 = new data available
  status = i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_STATUS_REG_M)

  if(status & 1) {
    //Values are stored as two's complement
    X = (i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_OUT_X_H_M) * 256) | i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_OUT_X_L_M)
    Y = (i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_OUT_Y_H_M) * 256) | i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_OUT_Y_L_M)
    Z = (i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_OUT_Z_H_M) * 256) | i2c1.readByteSync(LSM9DS1_A_ADDRESS_R,LSM9DS1_OUT_Z_L_M)
    abs = Math.sqrt(X**2+Y**2+Z**2)
  }

  i2c1.closeSync()

  return abs
}

module.exports = {
  readMagnetometer: readMagnetometer,
  turnOff: turnOff
}