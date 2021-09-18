import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Routes from "./Routes";


function App() {
  return (
    <Router>
      <div class="container-fluid py-3">
        <Header/>
          <Routes/>

        <Footer/>
      </div>
    </Router>
  );
}

export default App;
