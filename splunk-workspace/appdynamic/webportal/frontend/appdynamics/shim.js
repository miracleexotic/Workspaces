require("appdynamics").profile({
  debug: true,
  controllerHostName: '10.105.14.106',
  controllerPort: 80,
  controllerSslEnabled: false,  // Set to true if controllerPort is SSL
  accountName: 'customer1',
  accountAccessKey: '2d995a51-2ca7-4e88-a8ee-afa10fde6bc2', //required
  applicationName: 'WebPortal',
  tierName: 'Frontend',
  nodeName: 'node 68ea',
  logging: {
    'logfiles': [
      {
        'root_directory': '/tmp/appd',
        'filename': 'echo_%N.log',
        'level': 'TRACE',
        'max_size': 5242880,
        'max_files': 10
      }
    ]
  }
}); 
