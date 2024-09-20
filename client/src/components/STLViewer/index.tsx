import styled from "styled-components";
import FallbackRender from "../FallbackRender";
import LoadingTextModel from "./LoadingTextModel";
import { Canvas } from "@react-three/fiber";
import { Center, Environment, OrbitControls } from "@react-three/drei";
import { Suspense } from "react";
import { ErrorBoundary } from "react-error-boundary";
import STLModel from "./STLModel";

const StyledSTLViewer = styled.div`
  margin: 24px 12px 0 12px;
  width: calc(100% - 24px);
  border-radius: 8px;
  overflow: hidden;

  display: grid;
  place-items: center;
`;

export default function STLViewer() {
  return (
    <StyledSTLViewer>
      <ErrorBoundary fallbackRender={FallbackRender}>
        <Canvas
          shadows
          camera={{ position: [0, 50, 20], fov: 35 }}
          frameloop="demand"
        >
          <color attach="background" args={[0x888888]} />

          <Center top>
            <Suspense fallback={<LoadingTextModel />}>
              <STLModel />
            </Suspense>
          </Center>

          <OrbitControls minPolarAngle={0} maxPolarAngle={1.3} />
          <Environment preset="city" />
        </Canvas>
      </ErrorBoundary>
    </StyledSTLViewer>
  );
}
