import Modal from "@mui/material/Modal";
import styled from "styled-components";

interface _props {
  open: boolean;
  onClose: () => void;
}

const ModalBody = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(10px);
  display: grid;
  place-items: center;

  * {
    color: white;
  }
`;

const AppInformation = styled.div`
  width: 500px;
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;

  h2 {
    padding-top: 24px !important;
  }

  ol {
    padding-left: 36px;
    display: grid;
    grid-template-columns: 1fr;
    gap: 4px;
  }
`;

const CloseButton = styled.button`
  background-color: transparent;
  outline: none;
  border: 0;
  cursor: pointer;
  width: fit-content;
  margin: 24px auto;
  color: #9d9d9d;
`;

export default function AppInformationModal({ open, onClose }: _props) {
  return (
    <Modal
      open={open}
      onClose={onClose}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <ModalBody>
        <AppInformation>
          <h2>Hey! Joe here. Thanks for using VSSL!</h2>
          <p>
            VSSL is a hobby project that began with a desire to improve
            organization around the house through the use of 3D printed, slotted
            boxes. Then, with my web experience, I decided to wrap the script I
            wrote to generate these files in a web app and publish it to the
            world.
          </p>
          <h2>How do I use VSSL?</h2>
          <ol>
            <li>
              Measure the item you want to store along the x, y, and z axis.
            </li>
            <li>Determine how many slots you want along the x and y axis.</li>
            <li>
              Determine how thick you want the walls of the slots to be (1
              should be just fine)
            </li>
            <li>
              Use the "Wall Inset" option if you want the walls the fall below
              the edge of the box.
            </li>
            <li>Finally, set your lid options!</li>
            <li>Click the arrow button to see your render!</li>
            <li>
              Once your model is finalized, click the download button and store
              the file with the ".stl" extension.
            </li>
            <li>Load the file into your slicer of choice and print!</li>
          </ol>
          <h2>Thank you!</h2>
          <p>
            If you have any issues, feature suggestions, or just want to share
            your thoughts, feel free to reach out to me at&nbsp;
            <a href="mailto:joeboylson@gmail.com">joeboylson@gmail.com</a>.
          </p>
          <CloseButton onClick={onClose}>Close</CloseButton>
        </AppInformation>
      </ModalBody>
    </Modal>
  );
}
