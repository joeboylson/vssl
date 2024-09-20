import { useLoader } from "@react-three/fiber";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";
import { useSTLInputContext } from "../../context/STLInputs";

export default function STLModel() {
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
