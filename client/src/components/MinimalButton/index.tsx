import "./index.css";
import { WithChildren } from "../../types";

type _props = WithChildren & {
  onClick: (() => void) | ((event: React.MouseEvent<HTMLElement>) => void);
};

export default function MinimalButton({ onClick, children }: _props) {
  return (
    <button className="components-minimalbutton" onClick={onClick}>
      {children}
    </button>
  );
}
