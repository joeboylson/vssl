import styled from "styled-components";
import STLViewer from "../../components/STLViewer";
import { HEADER_HEIGHT } from "../../constants";
import STLInputs from "../../components/STLInputs";

const StyledHome = styled.div`
  height: calc(100vh - ${HEADER_HEIGHT}px);
  display: grid;
  grid-template-columns: 400px 1fr;
`;

export default function Home() {
  return (
    <StyledHome>
      <STLInputs />
      <STLViewer />
    </StyledHome>
  );
}
