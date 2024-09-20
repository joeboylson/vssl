import { Text } from "@react-three/drei";

export default function LoadingTextModel() {
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
