import { Canvas, useLoader } from "@react-three/fiber";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";
import { Center, Environment, OrbitControls, Text } from "@react-three/drei";
import styled from "styled-components";
import { Suspense } from "react";
import { useSTLInputContext } from "../../context/STLInputs";
import { ErrorBoundary } from "react-error-boundary";
import FallbackRender from "../FallbackRender";

const StyledSTLViewer = styled.div`
  margin: 12px;
  width: calc(100% - 24px);
  border-radius: 8px;
  overflow: hidden;
`;

function Cube() {
  return (
    <Text
      scale={[1, 1, 1]}
      color="black" // default
      anchorX="center" // default
      anchorY="middle" // default
      rotation={[-Math.PI / 2, 0, 0]}
    >
      Loading...
    </Text>
  );
}

function Model() {
  const { url } = useSTLInputContext();
  const stl = useLoader(STLLoader, url);

  return (
    <mesh
      geometry={stl}
      castShadow
      receiveShadow
      scale={[0.1, 0.1, 0.1]}
      rotation={[-Math.PI / 2, 0, 0]}
    >
      <meshStandardMaterial />
    </mesh>
  );
}

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
            <Suspense fallback={<Cube />}>
              <Model />
            </Suspense>
          </Center>

          <OrbitControls minPolarAngle={0} maxPolarAngle={1.3} />
          <Environment preset="city" />
        </Canvas>
      </ErrorBoundary>
    </StyledSTLViewer>
  );
}
