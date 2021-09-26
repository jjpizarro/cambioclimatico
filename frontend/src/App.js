import "bootstrap/dist/css/bootstrap.min.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Routes from "./Routes";
import Auth from "./context/Auth";

function App() {
  return (
    <Auth>
      <div class="container-fluid py-3">

        <Header/>
           
        <Routes/> 

        <Footer/>
      
      </div>
    </Auth>
  );
}

export default App;
