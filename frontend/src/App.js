import "bootstrap/dist/css/bootstrap.min.css";
import Header from "./components/Header";
import Search from "./components/Search";
import ImageCard from "./components/ImageCard";
import { useState , useEffect } from "react";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import Welcome from "./components/Welcome";
import axios from "axios";

const UNSPLASH_KEY = process.env.REACT_APP_UNSPLASH_KEY;
const REACT_APP_URL = process.env.REACT_APP_URL || "http://localhost:5050";

const App = () => {
  const [word, setWord] = useState("");
  const [images, setImages] = useState([]);
  // console.log(images);


  const getImages = async () =>{
      try{
        const res = await axios.get(`${REACT_APP_URL}/images`)
        setImages(res.data || [])
      }
      catch(error){
        console.log(error)
      }
  }

  useEffect(() =>  {getImages()},[])

  const handleSearchSubmit = async (e) => {
    e.preventDefault();
    // console.log(word);

    // with fetch
    // const response = await fetch(

    //fetch returns a promise
    // `https://api.unsplash.com/photos/random/?query=${word}&client_id=${UNSPLASH_KEY}`
    //   `${REACT_APP_URL}/new-images?query=${word}`
    // );
    // const data = await response.json();
    // setImages([{ ...data, title: word }, ...images]);
    // setWord("");

    // with axios

    console.log("Fetching the call");
    try {
      const response = await axios.get(
        `${REACT_APP_URL}/new-images?query=${word}`
      );
      console.log("data is retrieved");
      const data = response.data;

      setImages([{ ...data, title: word }, ...images]);
      console.log("clearing the search word");
    } catch (error) {
      console.log(error);
    }
    setWord("");
    // .then((res) => res.json())
    // .then((data) => {
    //   console.log(data);
    // })
    // .catch((err) => {
    //   console.log(err);
    // });
  };

  const handleDelete = (id) => {
    setImages(images.filter((image) => image.id != id));
  };

  //console.log(word); //anytime when the state of the component is change, the component is rerendered
  return (
    <div className="App">
      <Header title="Images Gallery" />
      <Search setWord={setWord} word={word} handleSubmit={handleSearchSubmit} />
      {/* { !!images.length && <ImageCard images={
        images[0]
      } />} */}
      <Container className="mt-4">
        {images.length ? (
          <Row xs={1} lg={3} md={2}>
            {images.map((image, i) => (
              <Col className="pb-3" key={i}>
                <ImageCard images={image} deleteImage={handleDelete} />
              </Col>
            ))}
          </Row>
        ) : (
          <Welcome />
        )}
      </Container>
    </div>
  );
};

export default App;
