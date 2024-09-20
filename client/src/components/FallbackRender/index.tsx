import { FallbackProps } from "react-error-boundary";

export default function FallbackRender({ error }: FallbackProps) {
  const errorMessageString: string = error.message.toString();

  if (errorMessageString.includes("TOO MANY REQUESTS"))
    return (
      <div>
        <p>Something went wrong:</p>
        <p>Too many requests</p>
      </div>
    );

  return (
    <div>
      <p>Something went wrong:</p>
      <pre style={{ color: "red" }}>{error.message}</pre>
    </div>
  );
}
