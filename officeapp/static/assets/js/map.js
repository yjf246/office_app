// function execute(){
//     const boxes = document.querySelectorAll('[role^="button"]');
//     // const boxes = document.querySelectorAll('[id^="div"]');
//     alert("hello_1");
//     function addClickHandler(box) {
//         box.addEventListener('click', function () {
//             alert("hello");
//             // // Remove click class from all boxes
//             // boxes.forEach(box => box.classList.remove('active'));

//             // // Add click class to the clicked box
//             // box.classList.add('active');
//         });
//     }
//     function handleElementFound(boxes) {
//         alert("function execute",boxes.length);

//         function addClickHandler(box) {
//             // box.addEventListener('click', function () {
//             //     alert("hello");
//             // });
//             alert("HELLO");
//         }

//         boxes.forEach(addClickHandler);
//     }

//     function checkForElement() {
//       const element = document.querySelectorAll('[tabindex^="0"]');
//       alert(element.length);
//       if (element.length>0) {
//         handleElementFound(element);
//       } else {
//         alert("na malyu");
//         // If element is not found, set up MutationObserver
//         const observer = new MutationObserver(() => {
//           const newElement = document.querySelectorAll('[tabindex^="0"]');
//           if (newElement) {
//             observer.disconnect(); // Stop observing once the element is found
//             handleElementFound(newElement);
//           }
//         });

//         // Start observing the document for changes
//         observer.observe(document, { childList: true, subtree: true });
//       }
//     }

//     // Call the function to start checkin for the element
//     checkForElement();

//     boxes.forEach(addClickHandler);
// }



