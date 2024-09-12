import "./index.css";
import { Canvas, useLoader } from "@react-three/fiber";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";
import { CameraControls } from "@react-three/drei";

export default function STLViewer() {
  const stl = useLoader(STLLoader, "generate-cube-stl");

  return (
    <div id="stl-viewer">
      <p>STL Viewer</p>
      <Canvas shadows camera={{ position: [10, 10, 10] }}>
        <ambientLight intensity={0.2} />
        <directionalLight color="red" position={[0, 0, 5]} />
        <mesh geometry={stl} castShadow receiveShadow>
          <meshStandardMaterial color={"orange"} />
        </mesh>
        <CameraControls makeDefault />
      </Canvas>
    </div>
  );
}
