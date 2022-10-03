import Heading from "./Components/Heading";
import Paragraph from "./Components/Paragraph";
var react = require("react");
const reactDom = require("react-dom");

// // reactDom.render(what to render,where to render);
// // reactDom.render(<h1>Hello World</h1>,
// // document.getElementById("root"));


// // var h1 = document.createElement("h1");
// // h1.innerHTML = "Hello World";
// // document.getElementById("root").appendChild(h1);
// function Heading(){
//   return <h1>Hello World</h1>;
// }
reactDom.render(
  <div>
    <Heading />
    <Paragraph />
    {/* <p> you cant learn anything </p> */}
   </div>,
   document.getElementById("root")
);

// thisIsAtTree
