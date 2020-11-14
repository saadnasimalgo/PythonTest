const config = require('./nodeTest')

function main(input) {
  const newConfig = Object.assign( {}, config)
  for(let key of Object.keys(config)){
    newConfig[key] = config[key]
    if(typeof config[key] === 'object'){
      for(let subObject of Object.keys(config[key])){
        if(config[key][subObject] === 'object'){
          newConfig[subObject] =  JSON.stringify(config[key][subObject])
          newConfig[key][subObject] = JSON.stringify(config[key][subObject])
        }else {
          newConfig[subObject] = JSON.stringify(config[key][subObject])
        }
      }
    }
  }
  console.log(newConfig);
  let modifiedInput = input.split('${--' ).join('${')
  modifiedInput = '`' + modifiedInput.split('${' ).join('${newConfig.') + '`'
  console.log(eval(modifiedInput))
}
main('${sparkCommand} --deploy-mode ${deployMode} --packages ${packages} --jars ${jars} --py-files ${--pyFiles} ${spark_application.options} ${spark_application.app} { \\"appName\\": ${spark_application.appName}}')
