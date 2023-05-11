import React from 'react';
import {Jumbotron , Button} from 'react-bootstrap';

const Welcome = () => {
return(

    <Jumbotron>
  <h1>Image Gallery</h1>
  <p>
   This is a python and react web applications
  </p>
  <p>
    <Button  href="https://unsplash.com" target="_blank">Learn more</Button>
  </p>
</Jumbotron>
)

}

export default Welcome;